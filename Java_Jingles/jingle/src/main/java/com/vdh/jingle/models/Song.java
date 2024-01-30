package com.vdh.jingle.models;

import java.util.Date;

import org.springframework.format.annotation.DateTimeFormat;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.PrePersist;
import jakarta.persistence.PreUpdate;
import jakarta.persistence.Table;
import jakarta.validation.constraints.NotEmpty;
import jakarta.validation.constraints.Size;

@Entity
@Table(name="songs")
public class Song {

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
	private Date yearAdded;
	
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
}
