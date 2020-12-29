package com.example.little.model;

import java.util.List;

public class Littles {

    private List<Little> Littles;

    public Littles(List<Little> Littles) {
        this.Littles = Littles;
    }

    public Littles() {}

    public List<Little> getLittles() {
        return Littles;
    }

    public void setLittles(List<Little> Littles) {
        this.Littles = Littles;
    }
}
