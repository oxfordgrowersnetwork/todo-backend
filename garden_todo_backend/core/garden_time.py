class GardenTime:
    def __init__(self, start_month, end_month):
        if start_month < 1 or start_month > 12:
            raise ValueError(f'Starting month not valid: {start_month}')

        if end_month < 1 or end_month > 12:
            raise ValueError(f'Ending month not valid: {start_month}')

        self.start_month = start_month
        self.end_month = end_month
