package org.example.models;

import jakarta.persistence.*;
import java.util.List;

@Entity
@Table(name = "estados")
public class Estado {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String nombre;

    @Column(nullable = false)
    private String ambito;

    // Constructor vacío requerido por JPA
    public Estado() {}

    // Constructor para facilitar la creación
    public Estado(String nombre, String ambito) {
        this.nombre = nombre;
        this.ambito = ambito;
    }

    //Metodos GET y SET
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getAmbito() {
        return this.ambito;
    }

    public void setAmbito(String ambito) {
        this.ambito = ambito;
    }

    public boolean esAmbitoSismografo() {
        return "sismografo".equalsIgnoreCase(this.ambito);
    }

    public boolean esFueraDeServicio() {
        return "Fuera de servicio".equalsIgnoreCase(this.nombre);
    }

    public boolean esAmbitoOrden() {
        return "orden".equalsIgnoreCase(this.ambito);
    }

    public boolean esCerrada() {
        return "Cerrada".equalsIgnoreCase(this.nombre);
    }

    public boolean esFinalizada() {
        return "Realizada".equalsIgnoreCase(this.nombre);
    }

    //public static List<Estado> obtenerEstados() {
    //    return List.of(values());
    //}
}

