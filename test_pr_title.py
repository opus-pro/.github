#!/usr/bin/env python3
"""
Test script for PR title validation regex using unittest framework.
Tests all the good and bad cases according to the requirements.
"""

import re
import json
import unittest
from pathlib import Path


class PRTitleValidationTest(unittest.TestCase):
    """Test cases for PR title validation regex"""

    @classmethod
    def setUpClass(cls):
        """Load the regex pattern from configuration file"""
        config_path = Path(__file__).parent / "pull_request_title.json"
        with open(config_path, 'r') as f:
            config = json.load(f)
        cls.regex_pattern = config['CHECKS']['regexp']
        cls.pattern = re.compile(cls.regex_pattern)

        # Good cases - should match the regex
        cls.good_cases = [
            "feat: add new authentication system",
            "fix: resolve memory leak in parser",
            "docs: update installation guide",
            "refactor: simplify user management logic",
            "test: add unit tests for api endpoints",
            "chore: update dependencies to latest versions",
            "[URGENT] fix: critical security vulnerability patch",
            "[FEATURE] feat: implement advanced search functionality",
            "perf: optimize database query performance significantly",
            "style: improve code formatting and readability standards"
        ]

        # Bad cases - should NOT match the regex
        cls.bad_cases = [
            # Double spaces after colon
            "feat:  enhance",
            "refactor: director don't  output result",
            "[hook-scripts] fix: fix hook-scripts object  (#2948)",
            "feat: trailing space ",
            "feat: double trailing space  ",

            # Uppercase type or first letter
            "Feat: blabla",
            "Fix: something wrong",
            "DOCS: update readme",

            # Too short titles
            "fix: bug",
            "feat: add",
            "docs: fix",

            # Too long titles
            "feat: this is a really really really really really really really really really really really really long message, do something something something something something something",

            # Ending with period
            "fix: bug something.",
            "feat: add new feature.",
            "docs: update documentation.",

            # Double dashes
            "fix: lirian--fix-some-thing",
            "feat: implement--new--feature",
            "refactor: clean--up--old--code",

            # Additional edge cases
            "invalidtype: some message",
            ": missing type",
            "feat:",  # missing message
            "feat:add",  # missing space
        ]

    def test_good_cases_should_pass(self):
        """Test that all good cases match the regex"""
        for title in self.good_cases:
            with self.subTest(title=title):
                self.assertIsNotNone(
                    self.pattern.match(title),
                    f"Good case should pass but failed: '{title}'"
                )

    def test_bad_cases_should_fail(self):
        """Test that all bad cases are rejected by the regex"""
        for title in self.bad_cases:
            with self.subTest(title=title):
                self.assertIsNone(
                    self.pattern.match(title),
                    f"Bad case should fail but passed: '{title}'"
                )

    def test_regex_pattern_loaded(self):
        """Test that regex pattern is loaded correctly"""
        self.assertIsNotNone(self.regex_pattern)
        self.assertIsInstance(self.regex_pattern, str)
        self.assertGreater(len(self.regex_pattern), 0)


if __name__ == "__main__":
    unittest.main()
