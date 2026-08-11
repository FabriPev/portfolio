package org.example.dao;

import org.example.models.Estado; // Importa tu entidad Estado
import org.example.util.HibernateUtil;
import org.hibernate.Session;

import java.util.Collections;
import java.util.List;

public class EstadoDao {

    /**Este metodo reemplaza al antiguo metodo estatico que existia en el enum Estado.
     * Su responsabilidad es consultar la base de datos y devolver una lista
     * de todos los registros de la tabla 'estados'.*/
    public List<Estado> obtenerEstados() {
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            // Usamos HQL para traer todas las instancias de la entidad "Estado".
            return session.createQuery("FROM Estado", Estado.class).list();
        } catch (Exception e) {
            System.err.println("Error al obtener los estados desde la base de datos: " + e.getMessage());
            e.printStackTrace();
            // Devolver una lista vacía para que el programa continúe funcionando.
            return Collections.emptyList();
        }
    }
}