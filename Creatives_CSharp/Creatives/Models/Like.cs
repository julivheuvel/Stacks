#pragma warning disable CS8618
using System.ComponentModel.DataAnnotations;

namespace Creatives.Models;

public class Like
{
    [Key]
    public int LikeId { get; set; }
    // ================
    
    public DateTime CreatedAt { get; set; } = DateTime.Now;
    // ================

    public DateTime UpdatedAt { get; set; } = DateTime.Now;
    // ================




    //! ===================================
    //! Relationships
    //! ===================================
    public int UserId { get; set; }
    public User? User { get; set; }
    public int ArtId { get; set; }
    public Art? Art { get; set; }
    
}