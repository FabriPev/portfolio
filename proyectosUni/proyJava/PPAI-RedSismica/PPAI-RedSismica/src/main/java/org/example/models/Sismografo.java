package org.example.models;

import jakarta.persistence.*;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

@Entity
@Table(name = "sismografos")
public class Sismografo {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "identificador_sismografo", nullable = false, unique = true)
    private int identificadorSismografo;

    @Column(name = "fecha_adquisicion", length = 50)
    private String fechaAdquisicion;

    @Column(name = "nro_serie")
    private int nroSerie;

    @OneToOne(mappedBy = "sismografo")
    private EstacionSismologica estacion;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "estado_actual_id", nullable = false)
    private Estado estadoActual;

    @OneToMany(mappedBy = "sismografo", cascade = CascadeType.ALL, fetch = FetchType.EAGER)
    private List<CambioEstado> cambiosEstado;

    public Sismografo() {
        // Constructor vacío requerido por JPA
        this.cambiosEstado = new ArrayList<>();
    }

    public Sismografo(int identificadorSismografo, String fechaAdquisicion, int nroSerie, Estado estadoInicial) {
        this.identificadorSismografo = identificadorSismografo;
        this.nroSerie = nroSerie;
        this.fechaAdquisicion = fechaAdquisicion;
        this.cambiosEstado = new ArrayList<>();
        this.estadoActual = estadoInicial;
        CambioEstado cambioInicial = new CambioEstado(null, null, null, null, null, null, List.of());
        cambioInicial.setEstado(this.estadoActual);
        cambioInicial.setSismografo(this);
        this.cambiosEstado.add(cambioInicial);
    }

    // Métodos GET y SET
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public int getIdentificadorSismografo() {
        return this.identificadorSismografo;
    }

    public void setIdentificadorSismografo(int identificadorSismografo) {
        this.identificadorSismografo = identificadorSismografo;
    }

    public int getNroSerie() {
        return this.nroSerie;
    }

    public void setNroSerie(int nroSerie) {
        this.nroSerie = nroSerie;
    }

    public String getFechaAdquisicion() {
        return this.fechaAdquisicion;
    }

    public void setFechaAdquisicion(String fechaAdquisicion) {
        this.fechaAdquisicion = fechaAdquisicion;
    }

    public Estado getEstadoActual() {
        return this.estadoActual;
    }

    public Estado setEstadoActual(Estado estadoActual) {
        return this.estadoActual = estadoActual;
    }

    public List<CambioEstado> getCambiosEstado() {
        return cambiosEstado;
    }

    public void setCambiosEstado(List<CambioEstado> cambiosEstado) {
        this.cambiosEstado = cambiosEstado;
    }


    public void enviarAReparar(Empleado responsableInspeccion, List<MotivoTipo> motivoSeleccionado, List<String> comentarioIngresado, String horaActual, String fechaActual, Estado estadoFueraDeServicio) {
        for (CambioEstado cambio : this.cambiosEstado) {
            if (cambio.esActual()) {
                cambio.setFechaHoraFin(fechaActual, horaActual);
            }
        }

        crearCE(responsableInspeccion, motivoSeleccionado, comentarioIngresado, horaActual, fechaActual, estadoFueraDeServicio);
    }

    public void crearCE(Empleado responsableInspeccion, List<MotivoTipo> motivosSeleccionado, List<String> comentarioIngresado, String horaActual, String fechaActual, Estado estadoFueraDeServicio) {
        // Usamos el parámetro en lugar de la constante estática
        CambioEstado nuevoCambio = new CambioEstado(fechaActual, horaActual, null, null, estadoFueraDeServicio, responsableInspeccion, null);

        this.estadoActual = estadoFueraDeServicio; // Actualizamos el estado actual
        nuevoCambio.setEstado(estadoFueraDeServicio);
        this.cambiosEstado.add(nuevoCambio);

        List<MotivoFueraServicio> comMotivos;
        if (comentarioIngresado == null) {
            comMotivos = new ArrayList<>();
        } else {
            comMotivos = comentarioIngresado.stream()
                    .map(texto -> new MotivoFueraServicio(texto))
                    .collect(Collectors.toList());
        }

        nuevoCambio.crearMotivoFS(comMotivos);
        System.out.println("Motivos fueraseleeccionados: " + motivosSeleccionado);
    }
}
