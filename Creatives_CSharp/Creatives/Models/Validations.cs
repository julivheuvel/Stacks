using System.ComponentModel.DataAnnotations;
using System.Text.RegularExpressions;

namespace Creatives.Models;




// ! ==================================================
// ! CUSTOM VALIDATIONS
// ! ==================================================


// ===============
//  MUST BE UNIQUE EMAIL
// ===============
public class UniqueEmailAttribute : ValidationAttribute
{
    protected override ValidationResult? IsValid(object? value, ValidationContext validationContext)
    {
        if (value == null)
        {
            // if value is empty
            return new ValidationResult("Email is required!");
        }

        // This will connect us to our database since we are not in our Controller
        CreativesContext db = (CreativesContext)validationContext.GetService(typeof(CreativesContext));
        // Check to see if there are any records of this email in our database
        if (db.Users.Any(e => e.Email == value.ToString()))
        {
            // If yes, throw an error
            return new ValidationResult("Email is already in use!");
        }
        else
        {
            // If no, proceed
            return ValidationResult.Success;
        }
    }
}
