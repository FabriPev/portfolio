import { Sequelize } from 'sequelize';
import path from 'path';
import { fileURLToPath } from 'url';

// Para obtener __dirname en ES Modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Ruta absoluta hacia data/pymes.db
const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, '../data/pymes.db'),
  define: {
    freezeTableName: true,
    timestamps: false,
  },
  logging: console.log, // Para ver las queries SQL (opcional)
});

export default sequelize;