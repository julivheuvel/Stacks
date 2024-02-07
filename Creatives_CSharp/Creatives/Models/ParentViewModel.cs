#pragma warning disable CS8618
namespace Creatives.Models;

public class ParentViewModel
{

    // ================
    // User
    // ================
    public User User { get; set; }
    public List<User> AllUsers { get; set; }


    // ================
    // Art
    // ================
    public Art Art { get; set; }
    public List<Art> AllArt { get; set; }
        

    // ================
    // Likes
    // ================
    public Like Like { get; set; }
    public List<Like> AllLikes { get; set; }
    



}