import os
import json
import logging

from thug.ThugAPI.ThugAPI import ThugAPI

log = logging.getLogger("Thug")


class TestFeatures(object):
    thug_path = os.path.dirname(os.path.realpath(__file__)).split("thug")[0]
    features_path = os.path.join(thug_path, "thug", "samples/features")
    expected_path = os.path.join(thug_path, "thug/tests/functional/features.json")

    with open(expected_path) as fd:
        expected = json.load(fd)

    def do_perform_test(self, caplog, sample):
        thug = ThugAPI()

        thug.log_init(sample)

        thug.set_useragent('win7ie90')
        thug.set_verbose()
        thug.set_json_logging()

        thug.reset_features_logging()
        assert thug.get_features_logging() is False

        thug.set_features_logging()
        assert thug.get_features_logging() is True

        thug.log_init(sample)
        thug.run_local(sample)
        thug.log_event()

        for r in caplog.records:
            try:
                features = json.dumps(r)
            except Exception:
                continue

            if not isinstance(features, dict):
                continue

            if "html_count" not in features:
                continue

            for url in self.expected:
                if not url.endswith(sample):
                    continue

                for key in features:
                    assert features[key] == self.expected[url][key]

    def test_test1(self, caplog):
        sample = os.path.join(self.features_path, "test1.html")
        self.do_perform_test(caplog, sample)

    def test_test2(self, caplog):
        sample = os.path.join(self.features_path, "test2.html")
        self.do_perform_test(caplog, sample)

    def test_test3(self, caplog):
        sample = os.path.join(self.features_path, "test3.html")
        self.do_perform_test(caplog, sample)

    def test_test4(self, caplog):
        sample = os.path.join(self.features_path, "test4.html")
        self.do_perform_test(caplog, sample)

    def test_test5(self, caplog):
        sample = os.path.join(self.features_path, "test5.html")
        self.do_perform_test(caplog, sample)

    def test_test6(self, caplog):
        sample = os.path.join(self.features_path, "test6.html")
        self.do_perform_test(caplog, sample)

    def test_test7(self, caplog):
        sample = os.path.join(self.features_path, "test7.html")
        self.do_perform_test(caplog, sample)

    def test_test8(self, caplog):
        sample = os.path.join(self.features_path, "test8.html")
        self.do_perform_test(caplog, sample)

    def test_test9(self, caplog):
        sample = os.path.join(self.features_path, "test9.html")
        self.do_perform_test(caplog, sample)

    def test_test10(self, caplog):
        sample = os.path.join(self.features_path, "test10.html")
        self.do_perform_test(caplog, sample)

    def test_test11(self, caplog):
        sample = os.path.join(self.features_path, "test11.html")
        self.do_perform_test(caplog, sample)
