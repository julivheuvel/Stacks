package com.vdh.jingle.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import com.vdh.jingle.models.Song;
import com.vdh.jingle.models.User;
import com.vdh.jingle.services.SongService;
import com.vdh.jingle.services.UserService;

import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;

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
	
	
//	=========================
//	ADD SONG
//	=========================
	@GetMapping("/songs/add")
	public String newSong(@ModelAttribute("newSong") Song newSong, Model model, HttpSession session, RedirectAttributes redirectAttributes) {
		Long loggedInUserId = (Long)session.getAttribute("user_id");
		
		if(loggedInUserId == null) {
			redirectAttributes.addFlashAttribute("notAllowed", "Must be logged in to view this page!!!");
			return "redirect:/";
		}
		
		User user = userService.findUser(loggedInUserId);
    	model.addAttribute("user", user);
		
		return "addMusic.jsp";
	}
	
	@PostMapping("/songs/new")
	public String creatSong(@Valid @ModelAttribute("newSong") Song newSong, BindingResult result, HttpSession session, RedirectAttributes redirectAttributes) {
		Long loggedInUserId = (Long)session.getAttribute("user_id");
		
		if(loggedInUserId == null) {
			redirectAttributes.addFlashAttribute("notAllowed", "Must be logged in to view this page!!!");
			return "redirect:/";
		}
		
		if(result.hasErrors()) {
			return "addMusic.jsp";
		}
		
		User user = userService.findUser(loggedInUserId);
		newSong.setUser(user);
		
		songService.create(newSong);
		
		return "redirect:/dashboard";
		
	}
	
//	=========================
//	UPDATE SONG
//	=========================	
	 @GetMapping("/songs/{id}/edit")
	 public String editSong(@PathVariable("id") Long id, Model model, 
	    		HttpSession session, RedirectAttributes redirectAttributes) {
	    	
	 	Long loggedInUserId = (Long)session.getAttribute("user_id");
    	
    	if(loggedInUserId == null) {
    		redirectAttributes.addFlashAttribute("notAllowed", "Must be logged in to view this page!!!" );
    		return "redirect:/";
    	}
    	
    	
    	Song song = songService.findSong(id);
    	System.out.println("==================");
    	System.out.println(song);
    	System.out.println("==================");
    	model.addAttribute("song", song);
    	
    	return "updateMusic.jsp";
    }
	 
	 @PutMapping("/songs/{id}/update")
	 public String updateSong(@Valid @ModelAttribute("song") Song updateSong, BindingResult result) {
		  if(result.hasErrors()) {
			  return "updateMusic.jsp";
		  }
		 return "redirect:/dashboard";
	 }
	    



}
