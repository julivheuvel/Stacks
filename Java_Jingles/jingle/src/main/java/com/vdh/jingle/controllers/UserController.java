package com.vdh.jingle.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import com.vdh.jingle.models.LoginUser;
import com.vdh.jingle.models.Song;
import com.vdh.jingle.models.User;
import com.vdh.jingle.services.SongService;
import com.vdh.jingle.services.UserService;

import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;

@Controller
public class UserController {
	
	@Autowired
	private UserService userService;
	
	@Autowired
	private SongService songService;
	
	@GetMapping("/")
	public String index() {
		
		return "index.jsp";
	}
	
	
//	======================
//	REGISTER
//	======================
	@GetMapping("/register")
	public String register(Model model) {
		model.addAttribute("newUser", new User());
		return "register.jsp";
	}
	
	@PostMapping("/reg")
	public String reg(@Valid @ModelAttribute("newUser") User newUser, BindingResult result, Model model, HttpSession session) {
		userService.register(newUser,  result);
		
		if(result.hasErrors()) {
			return "register.jsp";
		}
		
		session.setAttribute("user_id", newUser.getId());
		return "redirect:/dashboard";
	}
	
	
//	======================
//	LOGIN
//	======================
	@GetMapping("/login")
	public String login(Model model) {
		
		model.addAttribute("newLogin", new LoginUser());
		return "login.jsp";
	}
	
	@PostMapping("/log")
	public String log(@Valid @ModelAttribute("newLogin") LoginUser newLogin, BindingResult result, Model model, HttpSession session) {
		
		User user = userService.login(newLogin, result);
		
		if(result.hasErrors()) {
			
			return "login.jsp";
		}
		
		session.setAttribute("user_id", user.getId());	
		
		return "redirect:/dashboard";
	}
	
	
	
//	======================
//	LOGOUT
//	======================
	@GetMapping("/logout")
	public String logout(HttpSession session) {
		
		session.removeAttribute("user_id");
		
		return "redirect:/";
	}

//	======================
//	DASHBOARD
//	======================
	@GetMapping("/dashboard")
	public String dashboard(HttpSession session, Model model, RedirectAttributes redirectAttributes) {
		
		Long loggedInUserId = (Long)session.getAttribute("user_id");
		
		if(loggedInUserId == null) {
			redirectAttributes.addFlashAttribute("notAllowed", "Must be logged in to view this page!!!");
			return "redirect:/";
		}
		
		
		User loggedInUser = this.userService.findUser(loggedInUserId);
		
		model.addAttribute("loggedInUser", loggedInUser);
		
		List<Song> songs = songService.getAll();
		model.addAttribute("songs", songs);
		
		return "dashboard.jsp";
	}
}
