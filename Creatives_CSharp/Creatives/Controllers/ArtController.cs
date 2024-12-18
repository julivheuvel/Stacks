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
    // Accesing Database for Manipulation
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
    public IActionResult Dashboard(string search)
    {
        if(!loggedIn || uid == null)
        {
            return RedirectToAction("Welcome", "User");
        }

        if(search != null)
        {
            List<Art> filteredArt = db.Arts
                .Include(a => a.Poster)
                .Include(a => a.Followers)
                .Where(a => a.Artist.Contains(search)
                    || a.Name.Contains(search))
                .ToList();
            return View("Dashboard", filteredArt);
            
        }

        // ========
        // Get All Art
        // ========
        List<Art> allArt = db.Arts
            .Include(a => a.Poster)
            .Include(a => a.Followers)
            .ToList();



        return View("Dashboard", allArt);
    }

    // ================
    // New Art Render
    // ================
    [HttpGet("/art/new")]
    public IActionResult New()
    {
        if(!loggedIn)
        {
            return RedirectToAction("Welcome", "User");
        }
        return View("NewArt");
    }

    // ================
    // New Art Post
    // ================
    [HttpPost("/art/create")]
    public IActionResult CreateArt(Art newArt)
    {
        if(!loggedIn || uid == null)
        {
            return RedirectToAction("Index", "Users");
        }

        
        if(!ModelState.IsValid)
        {
            Console.WriteLine("======================");
            Console.WriteLine("Invalid!!!!");
            Console.WriteLine("======================");

            return New();
            }

        newArt.UserId = (int)uid;

        db.Arts.Add(newArt);
        db.SaveChanges();
        return RedirectToAction("Dashboard");
    }

    // ================
    // View Art Render
    // ================
    [HttpGet("/art/{artId}/view")]
    public IActionResult ViewArt(int artId)
    {

        if(!loggedIn)
        {
            return RedirectToAction("Welcome", "User");
        }

        // find the id
        Art? art = db.Arts.FirstOrDefault(p => p.ArtId == artId);

        // if id not found
        if(art == null)
        {
            return RedirectToAction("Dashboard");
        }

        return View("ViewArt", art);
    }

    // ================
    // Edit Art Render
    // ================
    [HttpGet("/art/{artId}/edit")]
    public IActionResult EditArt(int artId)
    {

        if(!loggedIn)
        {
            return RedirectToAction("Welcome", "User");
        }

        // find the id
        Art? art = db.Arts.FirstOrDefault(p => p.ArtId == artId);

        // if id not found
        if(art == null)
        {
            return RedirectToAction("Dashboard");
        }

        return View("EditArt", art);
    }

    // =======================
    // Edit Art Post
    // =======================
    [HttpPost("/art/{artId}/update")]
    public IActionResult UpdateArt(Art editedArt, int artId)
    {
        if(!loggedIn)
        {
            return RedirectToAction("Welcome", "User");
        }   
        
        if(!ModelState.IsValid)
        {   
            return EditArt(artId);
        }

        // does the art exist?
        Art? dbArt = db.Arts.FirstOrDefault(p => p.ArtId == artId);
        if(dbArt == null)
        {   
            return RedirectToAction("Dashboard");
        }

        dbArt.Name = editedArt.Name;
        dbArt.Artist = editedArt.Artist;
        dbArt.Description = editedArt.Description;
        dbArt.Price = editedArt.Price;
        dbArt.UpdatedAt = DateTime.Now;

        db.Arts.Update(dbArt);
        Console.WriteLine("====***********************=====");
        db.SaveChanges();


        return RedirectToAction("Dashboard");
    }

    // =======================
    // Delete Art
    // =======================
    [HttpPost("/art/{deletedArtId}/delete")]
    public IActionResult DeleteArt(int deletedArtId)
    {
        if(!loggedIn) {
            return RedirectToAction("Welcome", "User");
        }

        Art? art = db.Arts.FirstOrDefault(a => a.ArtId == deletedArtId);

        if(art != null)
        {
            db.Arts.Remove(art);
            db.SaveChanges();
        }

        return RedirectToAction("Dashboard");

    }

    // =======================
    // Like Art
    // =======================
    [HttpPost("/art/{artId}/like")]
    public IActionResult Like(int artId)
    {
        
        if(!loggedIn || uid == null)
        {
            return RedirectToAction("Welcome", "User");
        }   

    Like? existingLike = db.Likes
        .FirstOrDefault(l => l.ArtId == artId && l.UserId == (int) uid);

    if(existingLike == null)
    {
        Like newLike = new Like()
        {
            UserId = (int)uid,
            ArtId = artId
        };
        db.Likes.Add(newLike);
    }
    else
    {
        db.Likes.Remove(existingLike);
    }

    db.SaveChanges();

    return RedirectToAction("Dashboard");
    }

}