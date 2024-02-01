package com.vdh.jingle.services;

import java.util.Optional;

import org.mindrot.jbcrypt.BCrypt;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.validation.BindingResult;

import com.vdh.jingle.models.LoginUser;
import com.vdh.jingle.models.User;
import com.vdh.jingle.repositories.UserRepository;

@Service
public class UserService {

	@Autowired
	private UserRepository userRepo;
	
	public User register(User newUser, BindingResult result) {
        // this validation is to make sure the email of the new  user trying to register
		// is an email that is not already taken. Email must be unique!
    	if(userRepo.findByEmail(newUser.getEmail()).isPresent()) {
            result.rejectValue("email", "Unique", "This email is already in use!");
        }
        if(!newUser.getPassword().equals(newUser.getConfirm())) {
            result.rejectValue("confirm", "Matches", "The Confirm Password must match Password!");
        }
        if(result.hasErrors()) {
            return null;
        } else {
            String hashed = BCrypt.hashpw(newUser.getPassword(), BCrypt.gensalt());
            newUser.setPassword(hashed);
            return userRepo.save(newUser);
        }
    }
	
	
	public User login(LoginUser newLogin, BindingResult result) {
        if(result.hasErrors()) {
            return null;
        }
        
        // checking if we find a user in the db who has an email that was used in form
        Optional<User> potentialUser = userRepo.findByEmail(newLogin.getEmail());
        if(!potentialUser.isPresent()) {
            result.rejectValue("email", "Unique", "Unknown email!");
            return null;
        }
        
        // if user doesn't exist while logging in created validation message
        User user = potentialUser.get();
        
        // checking password that matches the db and seeing if they match
        if(!BCrypt.checkpw(newLogin.getPassword(), user.getPassword())) {
            result.rejectValue("password", "Matches", "Invalid Password!");
        }
        // if password doesn't match created another validation error message
        if(result.hasErrors()) {
            return null;
        } else {
            return user;
        }
    }
	
	public User findUser(Long id) {
    	return this.userRepo.findById(id).orElse(null);
    }
}
