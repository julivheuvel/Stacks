package com.vdh.jingle.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import com.vdh.jingle.services.UserService;

@Controller
public class UserController {
	
	@Autowired
	private UserService userService;
	
	@GetMapping("/")
	public String index() {
		
		return "index.jsp";
	}
	
	@GetMapping("/register")
	public String register() {
		
		return "register.jsp";
	}

}