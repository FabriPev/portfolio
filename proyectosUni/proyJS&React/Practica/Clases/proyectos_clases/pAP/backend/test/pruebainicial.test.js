import supertest from "supertest";
import app from "../index.js";

const request = supertest(app);

describe("Ejemplo simple, test que no falla", () => {
  it("Simplemente compruebo si true === true", () => {
    expect(true).toBe(true);
  });
});

describe("GET Backend inicial dds-backend!", () => {
  it("Debería devolver Backend inicial dds-backend!", async () => {
    const res = await request.get("/");
    expect(res.statusCode).toEqual(200);
    expect(res.text).toEqual('Backend inicial dds-backend!');
  });
});

describe("GET _isalive", () => {
  it("Deberia devolver ejecutándose desde ...", async () => {
    const res = await request.get("/_isalive");
    expect(res.statusCode).toEqual(200);
    expect(res.text).toContain('Ejecutandose desde:');
  });
});

describe("GET 404", () => {
  it("Debería devolver error 404 y su texto apropiado", async () => {
    const res = await request.get("/urlinexistente");
    expect(res.statusCode).toEqual(404);
    expect(res.text).toEqual("No encontrada!");
  });
});