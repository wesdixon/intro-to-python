# Let's build a `Company` class, used to represent some company (Denver Beer Co., Qdoba, Chipotle, etc.).
#
#     1. In this class, we'll have the following attributes:
#
#         * `name` - `str` holding the name of the company
#         * `industry_type` - `str` holding what industry the company belongs to
#         * `num_employees` - `int` holding the number of employees the company has
#         * `total_revenue` - `float` holding the total revenue of the company
#
#     2. Instances of the `Company` class will have the following methods:
#
#         * `serve_customer` - this method will take in a `float` that is equal to the cost of serving some customer,
#         and then adjust the `total_revenue` by that cost.
#         * `gain_employees` - this method will take in a `list` that contains new employees that the company has
#         just brought on, and will update the `num_employees` attribute to take account of that.


class Company():

    def __init__(self, name, industry_type, num_employees, total_revenue):

        self.name = name
        self.industry_type = industry_type
        self.num_employees = num_employees
        self.total_revenue = total_revenue

    def serve_customer(self, cost_of_customer):

        self.total_revenue -= cost_of_customer

    def gain_employees(self, new_employees_lst):

        self.num_employees += len(new_employees_lst)


#Main Test Block

my_company = Company("Swipe", "Credit Cards", 222, 1234.56)

my_company.serve_customer(4.56)
print my_company.total_revenue

my_company.gain_employees(["Bob", "Sally", "Jane", "Anne"])
print my_company.num_employees
