package org.example.dao;

import org.example.models.MotivoTipo;
import org.example.util.HibernateUtil;
import org.hibernate.Session;
import java.util.Collections;
import java.util.List;

public class MotivoTipoDao {

    /**Este metodo es el reemplazo del antigui metodo obtenerMotivosFS().
     *Consulta la base de datos para traer todos los registros de la tabla "motivos_tipo".*/
    public List<MotivoTipo> obtenerMotivosFS() {
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            // Se usa HQL (Hibernate Query Language) para pedir todas las
            // instancias de la entidad MotivoTipo.
            return session.createQuery("FROM MotivoTipo", MotivoTipo.class).list();
        } catch (Exception e) {
            System.err.println("Error al obtener los motivos de tipo de la base de datos: " + e.getMessage());
            e.printStackTrace();
            // Devuelve una lista vacía para que la aplicación no falle.
            return Collections.emptyList();
        }
    }
}