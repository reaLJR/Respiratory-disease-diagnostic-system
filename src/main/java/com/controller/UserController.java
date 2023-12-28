package com.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class UserController {
    @RequestMapping("/login")
    public String login(@RequestParam(value = "userId", required = false) String userId){


        return "login";
    }
}
