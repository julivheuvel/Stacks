package com.vdh.jingle.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.vdh.jingle.models.Song;

@Repository
public interface SongRepository extends CrudRepository<Song, Long> {
	
//	Song findByUser(Long userID);
	
	List<Song> findAll();
	
}
