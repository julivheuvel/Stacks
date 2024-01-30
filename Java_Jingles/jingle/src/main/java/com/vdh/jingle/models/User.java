package com.vdh.jingle.models;

import java.util.Date;
import java.util.List;

import org.springframework.format.annotation.DateTimeFormat;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.JoinTable;
import jakarta.persistence.ManyToMany;
import jakarta.persistence.OneToMany;
import jakarta.persistence.PrePersist;
import jakarta.persistence.PreUpdate;
import jakarta.persistence.Table;
import jakarta.persistence.Transient;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotEmpty;
import jakarta.validation.constraints.Size;


@Entity
@Table(name="users")
public class User {
	
//	=================
//	FIELDS
//	=================
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	private Long id;
	
	@NotEmpty(message="First Name is required!")
	@Size(min=3, max=30, message="First Name must be between 3 and 30 characters")
	private String firstName;
	
	@NotEmpty(message="Last Name is required!")
	@Size(min=3, max=30, message="Last Name must be between 3 and 30 characters")
	private String lastName;
	
	@NotEmpty(message="Email is required!")
    @Email(message="Please enter a valid email!")
    private String email;
	
	@NotEmpty(message="Password is required!")
    @Size(min=8, max=128, message="Password must be between 8 and 128 characters")
    private String password;
    
    @Transient
    @NotEmpty(message="Confirm Password is required!")
    @Size(min=8, max=128, message="Confirm Password must be between 8 and 128 characters")
    private String confirm;
    
    @Column(updatable = false)
	@DateTimeFormat(pattern = "yyyy-MM-dd")
	private Date createdAt;
	
	@DateTimeFormat(pattern = "yyyy-MM-dd")
	private Date updatedAt;
	
	@PrePersist
	protected void onCreate() {
		this.createdAt = new Date();
	}
	
	@PreUpdate
	protected void onUpdate() {
		this.updatedAt = new Date();
	}
	
//	=================
//	RELATIONSHIPS
//	=================
	@OneToMany(mappedBy="user", fetch=FetchType.LAZY)
	private List<Song<> songs;
	
	@ManyToMany(fetch=FetchType.LAZY)
	@JoinTable(
			name = "users_liked_songs",
			joinColumns = @JoinColumn(name="user_id"),
			inverseJoinColumns = @JoinColumn(name="song_id")
			)
	private List<Song> songsLiked;
	
//	=================
//	CONSTRUCTORS
//	=================
	public User() {}
	
	public User(String firstName, String lastName, String email, String password, List<Song> songs, List<Song> songsLiked) {
		this.firstName = firstName;
		this.lastName = lastName;
		this.email = email;
		this.password = password;
		this.songs = songs;
		this.songsLiked = songsLiked;				
	}
	
//	=================
//	GETTERS AND SETTERS
//	=================
}
