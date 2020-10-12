class Stock:

    def __init__(self):
        self.current_ratio = None
        self.dte_grade = None
        self.bvps_grade = None
        self.eps_grade = None
        self.raw_stock_data = None
        self.ten_years_span = {}
    
    def set_current_ratio(self, current_ratio):
        self.current_ratio = current_ratio

    def set_grades(self, dte_grade, bvps_grade, eps_grade):
        self.dte_grade = dte_grade
        self.bvps_grade = bvps_grade
        self.eps_grade = eps_grade
    
    def set_raw_stock_data(self, raw_stock_data):
        self.raw_stock_data = raw_stock_data
    
    def set_ten_years_span(self, ten_years_span):
        self.ten_years_span = ten_years_span

    def perform_initial_test(self):
        if self.current_ratio < 1.5:
            return False
        if self.dte_grade == 0:
            return False
        if self.bvps_grade == 0:
            return False
        if self.eps_grade == 0:
            return False

        return True
    