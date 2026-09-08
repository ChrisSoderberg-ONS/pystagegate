import pandas as pd
import pytest
import os
from pystagegate.pipelines import (
    prov_fin_main,
    sex_ratio_national_profile,
    sex_ratio_main,
)


@pytest.mark.parametrize("config", ["test_config", "test_config_path"])
class TestPipelines:
    def test_prov_fin_dict(self, request, config):
        output = prov_fin_main(request.getfixturevalue(config))

        expected_output = pd.read_pickle("tests/data/prov_fin/prov_fin_output.pkl")

        pd.testing.assert_frame_equal(output, expected_output)

    def test_sex_ratio_national_profile_dict(self, request, config):
        sq_diff, year_agg, year_agg_adjusted = sex_ratio_national_profile(
            request.getfixturevalue(config)
        )

        expected_sq_diff = pd.read_pickle(
            "tests/data/sex_ratio/provisional_final_ssq.pkl"
        )
        expected_year_agg = pd.read_pickle("tests/data/sex_ratio/year_agg_ssq.pkl")
        expected_year_agg_adjusted = pd.read_pickle(
            "tests/data/sex_ratio/year_agg_adjusted_ssq.pkl"
        )

        pd.testing.assert_frame_equal(sq_diff, expected_sq_diff)
        pd.testing.assert_frame_equal(year_agg, expected_year_agg)
        pd.testing.assert_frame_equal(year_agg_adjusted, expected_year_agg_adjusted)

    def test_sex_ratio_main(self, request, config):
        sr, sr_national, sr_merged_ssq = sex_ratio_main(request.getfixturevalue(config))

        expected_sr = pd.read_pickle("tests/data/sex_ratio/sex_ratio_recoded.pkl")
        expected_sr_national = pd.read_pickle(
            "tests/data/sex_ratio/sex_ratio_national.pkl"
        )
        expected_sr_merged_ssq = pd.read_pickle(
            "tests/data/sex_ratio/sex_ratio_ssq.pkl"
        )

        pd.testing.assert_frame_equal(sr, expected_sr)
        pd.testing.assert_frame_equal(sr_national, expected_sr_national)
        pd.testing.assert_frame_equal(sr_merged_ssq, expected_sr_merged_ssq)
