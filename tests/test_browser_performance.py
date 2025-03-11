import pytest
import logging
import json
from io import StringIO
from src.browser_performance import log_browser_rendering_metrics

class TestBrowserPerformanceLogging:
    def setup_method(self):
        # Capture log output
        self.log_capture = StringIO()
        self.log_handler = logging.StreamHandler(self.log_capture)
        self.logger = logging.getLogger()
        self.logger.addHandler(self.log_handler)
        self.logger.setLevel(logging.INFO)

    def teardown_method(self):
        # Remove log handler
        self.logger.removeHandler(self.log_handler)
        self.log_capture.close()

    def test_valid_performance_metrics(self):
        performance_data = {
            "first_contentful_paint": 100,
            "largest_contentful_paint": 250,
            "cumulative_layout_shift": 0.05,
            "total_blocking_time": 50
        }
        
        log_browser_rendering_metrics(performance_data)
        
        log_output = self.log_capture.getvalue()
        assert "Browser Rendering Performance Metrics" in log_output
        assert all(str(value) in log_output for value in performance_data.values())

    def test_custom_logger_name(self):
        performance_data = {"fps": 60}
        
        log_browser_rendering_metrics(performance_data, logger_name="custom_browser_logger")
        
        log_output = self.log_capture.getvalue()
        assert "Browser Rendering Performance Metrics" in log_output

    def test_custom_log_level(self):
        performance_data = {"render_time": 150}
        
        log_browser_rendering_metrics(
            performance_data, 
            log_level=logging.DEBUG
        )
        
        log_output = self.log_capture.getvalue()
        assert "Browser Rendering Performance Metrics" in log_output

    def test_invalid_input_types(self):
        with pytest.raises(TypeError):
            log_browser_rendering_metrics("not a dictionary")
        
        with pytest.raises(TypeError):
            log_browser_rendering_metrics(123)
        
        with pytest.raises(ValueError):
            log_browser_rendering_metrics({})

    def test_complex_performance_data(self):
        performance_data = {
            "navigation_timing": {
                "dns_lookup": 20,
                "initial_connection": 30
            },
            "resource_timings": [
                {"name": "script.js", "duration": 50},
                {"name": "styles.css", "duration": 10}
            ]
        }
        
        log_browser_rendering_metrics(performance_data)
        
        log_output = self.log_capture.getvalue()
        assert "Browser Rendering Performance Metrics" in log_output
        assert "script.js" in log_output
        assert "styles.css" in log_output