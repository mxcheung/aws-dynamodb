package com.example.little.controller;

import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.example.little.model.Littles;
import com.example.little.service.LittlesService;

@RestController
public class LittlesController {

    @Autowired
    private LittlesService littlesService = new LittlesService();

    @RequestMapping(value="/Littles", method=RequestMethod.GET)
    public Littles getLittles(HttpServletResponse response,
            @RequestParam(value = "filter", required = false) String filter,
            @RequestParam(value = "value", required = false) String value ) {

        response.addHeader("Access-Control-Allow-Origin", "*");

        Littles Littles;

        if (filter != null)
            Littles = littlesService.queryLittleItems(filter, value);
        else
            Littles = littlesService.getAllLittles();

        return Littles;
    }

    @RequestMapping(value="/", method=RequestMethod.GET)
    public String healthCheckResponse() {
        return "Nothing here, used for health check. Try /littles instead.";
    }

}