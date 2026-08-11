package org.example.models;

import jakarta.persistence.*;

@Entity
@Table(name = "motivos_tipo")
public class MotivoTipo {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private String descripcion;

    // Constructor vacío requerido por JPA
    public MotivoTipo() {}

    public MotivoTipo(String descripcion) {
        this.descripcion = descripcion;
    }

    //Metodo GET y SET
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    @Override
    public String toString() {
        return this.descripcion;
    }

    //Otros métodos de MotivoTipo
    //public static List<MotivoTipo> obtenerMotivosFS() {
    //    return List.of(values());
    //}
}
