using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

using Creatives.Models;

public class ArtController : Controller
{
    // ===========
    // Getting User ID
    // ===========
    private int? uid
    {
        get
        {
            return HttpContext.Session.GetInt32("UUID");
        }
    }

    // ===========
    // Getting Logged In User
    // ===========
    private bool loggedIn
    {
        get
        {
            return uid != null;
        }
    }


    // ===========
    // Importing Database
    // ===========
    private CreativesContext db;
    public ArtController(CreativesContext context)
    {
        db = context;
    }

    // ================
    // Dashboard
    // ================
    [HttpGet("/dashboard")]
    public IActionResult Dashboard()
    {
        if(!loggedIn)
        {
            return RedirectToAction("Index", "Users");
        }

        return View("Dashboard");
    }
}