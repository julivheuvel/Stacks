#pragma warning disable CS8618
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Creatives.Models;

public class Art
{

    // ================
    // Art ID
    // ================
    [Key]
    public int ArtId { get; set; }

    // ================
    // Name
    // ================
    [Required(ErrorMessage=" is required!")]
    public string Name { get; set; }

    // ================
    // Artist
    // ================
    [Required(ErrorMessage=" is required!")]
    public string Artist { get; set; }
    
    // ================
    // Description
    // ================
    [Required(ErrorMessage=" is required!")]
    public string Description { get; set; }
    
    // ================
    // Price
    // ================
    [Required(ErrorMessage="Price is required!")]
    public double Price { get; set; }

    // ================
    // CreatedAt
    // ================
    public DateTime CreatedAt { get; set; } = DateTime.Now;

    // ================
    // UpdatedAt
    // ================
    public DateTime UpdatedAt { get; set; } = DateTime.Now;

    //! ===================================
    //! Relationships
    //! ===================================
    // ================
    // User - One to Many
    // ================
    public int UserId { get; set; }
    public User? Poster { get; set; }
    
    // ================
    // Likes - Many to Many
    // ================
    public List<Like> Followers { get; set; } = new List<Like>();
}