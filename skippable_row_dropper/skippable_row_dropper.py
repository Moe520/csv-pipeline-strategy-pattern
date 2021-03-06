class SkippableRowDropper:
    """
    Drops rows from a dataframe based on a strategy
    """
    def __init__(self, drop_rows_strategy):
        self.dropping_strategy = drop_rows_strategy

    def drop_bad_rows(self, data_ref, error_logger):
        """
        :param data_ref: Reference to a pandas dataframe
        :param error_logger: Will be used to report bad rows to a log file
        :return:
        """
        self.dropping_strategy.drop_bad_rows(self.dropping_strategy, data_ref, error_logger)
