import json
import logging
from typing import Dict, Any, Optional

def log_browser_rendering_metrics(performance_data: Dict[str, Any], 
                                   log_level: int = logging.INFO, 
                                   logger_name: Optional[str] = None) -> None:
    """
    Log browser rendering performance metrics with configurable logging.

    Args:
        performance_data (Dict[str, Any]): A dictionary containing performance metrics.
        log_level (int, optional): Logging level. Defaults to logging.INFO.
        logger_name (Optional[str], optional): Name of the logger. Defaults to None.

    Raises:
        TypeError: If performance_data is not a dictionary.
        ValueError: If performance_data is empty.
    """
    # Validate input
    if not isinstance(performance_data, dict):
        raise TypeError("Performance data must be a dictionary")
    
    if not performance_data:
        raise ValueError("Performance data cannot be empty")

    # Configure logger
    logger = logging.getLogger(logger_name or __name__)
    
    try:
        # Serialize metrics for comprehensive logging
        metrics_json = json.dumps(performance_data, indent=2)
        
        # Log the performance metrics
        logger.log(log_level, f"Browser Rendering Performance Metrics:\n{metrics_json}")
    
    except Exception as e:
        logger.error(f"Error logging performance metrics: {str(e)}")
        raise