package com.vdh.jingle.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.vdh.jingle.models.Song;
import com.vdh.jingle.repositories.SongRepository;

@Service
public class SongService {
	
	@Autowired
	private SongRepository songRepo;
	
	public List<Song> getAll() {
		return (List<Song>) songRepo.findAll();
	}
	
	public Song findSong(Long id) {
		Optional<Song> optionalSong = songRepo.findById(id);
		if(optionalSong.isPresent()) {
			return optionalSong.get();
		}
		else {
			return null;
		}
	}
	
	public void deleteSong(Song song) {
		songRepo.delete(song);
	}
}
