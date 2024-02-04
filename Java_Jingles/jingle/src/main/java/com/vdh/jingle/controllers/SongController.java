package com.vdh.jingle.controllers;

import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.model;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import com.vdh.jingle.models.Song;
import com.vdh.jingle.models.User;
import com.vdh.jingle.services.SongService;
import com.vdh.jingle.services.UserService;

import jakarta.servlet.http.HttpSession;

@Controller
public class SongController {
	
	@Autowired
	private UserService userService;
	
	@Autowired
	private SongService songService;
	
	public SongController(UserService userService, SongService songService) {
		this.userService = userService;
		this.songService = songService;
	}
	
	@GetMapping("/songs/new")
	public String newSong(@ModelAttribute("newSong") Song newSong, Model model, HttpSession session, RedirectAttributes redirectAttributes) {
		Long loggedInUserId = (Long)session.getAttribute("user_id");
		
		if(loggedInUserId == null) {
			redirectAttributes.addFlashAttribute("notAllowed", "Must be logged in to view this page!!!");
			return "redirect:/";
		}
		
		User user = userService.findUser(loggedInUserID);
    	model.addAttribute("user", user);
		
		return "addMusic.jsp";
	}

}
