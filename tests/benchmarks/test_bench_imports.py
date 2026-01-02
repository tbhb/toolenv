import importlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_codspeed.plugin import BenchmarkFixture
    from pytest_mock import MockerFixture


class TestBenchImportTime:
    def test_import_time_toolenv(
        self, benchmark: "BenchmarkFixture", mocker: "MockerFixture"
    ) -> None:
        def import_toolenv():
            _ = mocker.patch("sys.modules", {})
            _ = importlib.import_module("toolenv", "test_bench_imports")

        benchmark(import_toolenv)
