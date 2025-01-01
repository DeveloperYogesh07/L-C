#include <iostream>
#include <string>

// Employee Class - Represents the basic details of an employee
class Employee {
private:
    int id;
    std::string name;
    std::string department;
    bool working;

public:
    Employee(int empId, const std::string& empName, const std::string& empDepartment, bool isWorking)
        : id(empId), name(empName), department(empDepartment), working(isWorking) {}

    void terminateEmployee() {
        working = false;
        std::cout << "Employee " << name << " has been terminated." << std::endl;
    }

    bool isWorking() const {
        return working;
    }

    std::string getName() const { return name; }
    std::string getDepartment() const { return department; }
    int getId() const { return id; }
};

// EmployeeDatabase - Handles persistence of Employee data
class EmployeeDatabase {
public:
    void saveEmployeeToDatabase(const Employee& employee) {
        std::cout << "Employee " << employee.getName() << " saved to database." << std::endl;
    }
};

// EmployeeReport - Responsible for generating reports for Employee details
class EmployeeReport {
public:
    void printEmployeeDetailReportXML(const Employee& employee) {
        std::cout << "<Employee>\n"
                  << "  <Id>" << employee.getId() << "</Id>\n"
                  << "  <Name>" << employee.getName() << "</Name>\n"
                  << "  <Department>" << employee.getDepartment() << "</Department>\n"
                  << "  <Working>" << (employee.isWorking() ? "Yes" : "No") << "</Working>\n"
                  << "</Employee>" << std::endl;
    }

    void printEmployeeDetailReportCSV(const Employee& employee) {
        std::cout << employee.getId() << ", " << employee.getName() << ", "
                  << employee.getDepartment() << ", " << (employee.isWorking() ? "Yes" : "No")
                  << std::endl;
    }
};

// Example Usage
int main() {
    // Create an Employee
    Employee emp(1, "John Doe", "Engineering", true);

    // Save Employee to Database
    EmployeeDatabase db;
    db.saveEmployeeToDatabase(emp);

    // Generate Reports
    EmployeeReport report;
    report.printEmployeeDetailReportXML(emp);
    report.printEmployeeDetailReportCSV(emp);

    // Terminate Employee
    emp.terminateEmployee();
    std::cout << "Is Working: " << (emp.isWorking() ? "Yes" : "No") << std::endl;

    return 0;
}
