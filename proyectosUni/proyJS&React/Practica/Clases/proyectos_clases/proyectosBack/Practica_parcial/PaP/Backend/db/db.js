import { Sequelize} from "sequelize";
const sequelize = new Sequelize("sqlite::memory:")
export default sequelize

//Declaracion de la base de datos