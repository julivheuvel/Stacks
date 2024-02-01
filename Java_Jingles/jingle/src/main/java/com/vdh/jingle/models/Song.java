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
import jakarta.persistence.ManyToOne;
import jakarta.persistence.PrePersist;
import jakarta.persistence.PreUpdate;
import jakarta.persistence.Table;
import jakarta.validation.constraints.NotEmpty;
import jakarta.validation.constraints.Size;

@Entity
@Table(name="songs")
public class Song {
	
//	=================
//	FIELDS
//	=================
	@Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
	
	@NotEmpty(message="Name is required!")
    @Size(min=3, max=100, message="Name must be between 1 and 100 characters")
    private String name;
	
	@NotEmpty(message="Album is required!")
    @Size(min=3, max=100, message="Album must be between 1 and 100 characters")
    private String album;
	
	@NotEmpty(message="Artist is required!")
    @Size(min=3, max=100, message="Artist must be between 1 and 100 characters")
    private String artist;
	
	@DateTimeFormat(pattern = "yyyy-MM-dd")
	private Date dateAdded;
	
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
	@ManyToOne(fetch=FetchType.LAZY)
	@JoinColumn(name="user_id")
	public User user;
	
	
	@ManyToMany
	@JoinTable(
			name="users_liked_songs",
			joinColumns = @JoinColumn(name = "song_id"),
			inverseJoinColumns = @JoinColumn(name="user_id")
			)
	private List<User> usersLiked;
	
//	=================
//	CONSTRUCTORS
//	=================
	public Song() {}
	
	public Song(String name, String album, String artist, Date dateAdded, User user, List<User> usersLiked) {
		this.name = name;
		this.album = album;
		this.artist = artist;
		this.dateAdded = dateAdded;
		this.usersLiked = usersLiked;
	}
	
//	=================
//	GETTERS AND SETTERS
//	=================
	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getAlbum() {
		return album;
	}

	public void setAlbum(String album) {
		this.album = album;
	}

	public String getArtist() {
		return artist;
	}

	public void setArtist(String artist) {
		this.artist = artist;
	}

	public Date getDateAdded() {
		return dateAdded;
	}

	public void setDateAdded(Date dateAdded) {
		this.dateAdded = dateAdded;
	}

	public Date getCreatedAt() {
		return createdAt;
	}

	public void setCreatedAt(Date createdAt) {
		this.createdAt = createdAt;
	}

	public Date getUpdatedAt() {
		return updatedAt;
	}

	public void setUpdatedAt(Date updatedAt) {
		this.updatedAt = updatedAt;
	}

	public User getUser() {
		return user;
	}

	public void setUser(User user) {
		this.user = user;
	}

	public List<User> getUsersLiked() {
		return usersLiked;
	}

	public void setUsersLiked(List<User> usersLiked) {
		this.usersLiked = usersLiked;
	}	
	
}
