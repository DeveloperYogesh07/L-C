using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

public class CustomerSearch
{
    private readonly DatabaseContext db; // Assuming `db` is your database context

    public CustomerSearch(DatabaseContext databaseContext)
    {
        db = databaseContext;
    }

    /// <summary>
    /// Searches customers by country.
    /// </summary>
    public List<Customer> SearchByCountry(string country)
    {
        if (string.IsNullOrWhiteSpace(country))
            throw new ArgumentException("Country name cannot be null or empty.", nameof(country));

        return db.Customers
                 .Where(c => c.Country.Contains(country))
                 .OrderBy(c => c.CustomerID)
                 .ToList();
    }

    /// <summary>
    /// Searches customers by company name.
    /// </summary>
    public List<Customer> SearchByCompanyName(string companyName)
    {
        if (string.IsNullOrWhiteSpace(companyName))
            throw new ArgumentException("Company name cannot be null or empty.", nameof(companyName));

        return db.Customers
                 .Where(c => c.CompanyName.Contains(companyName))
                 .OrderBy(c => c.CustomerID)
                 .ToList();
    }

    /// <summary>
    /// Searches customers by contact person.
    /// </summary>
    public List<Customer> SearchByContact(string contact)
    {
        if (string.IsNullOrWhiteSpace(contact))
            throw new ArgumentException("Contact name cannot be null or empty.", nameof(contact));

        return db.Customers
                 .Where(c => c.ContactName.Contains(contact))
                 .OrderBy(c => c.CustomerID)
                 .ToList();
    }

    /// <summary>
    /// Exports customer data to a CSV format.
    /// </summary>
    public string ExportToCSV(List<Customer> data)
    {
        if (data == null || data.Count == 0)
            return string.Empty;

        var stringBuilder = new StringBuilder();

        foreach (var customer in data)
        {
            stringBuilder.AppendFormat(
                "{0},{1},{2},{3}", 
                customer.CustomerID, 
                customer.CompanyName, 
                customer.ContactName, 
                customer.Country
            );
            stringBuilder.AppendLine();
        }

        return stringBuilder.ToString();
    }
}
