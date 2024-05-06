-- Crear Collection "tipos_reactor"

db.createCollection("tipos_reactor", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         title: "Tipos de reactores",
         required: [ "tipo" ],
         properties: {
            tipo: {
               bsonType: "string",
               description: "'tipo' Debe ser una cadena de caracteres y no puede ser nulo"
            }
         }
      }
   }
} );

-- Crear Collection "ubicaciones"

db.createCollection("ubicaciones", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         title: "Ubicaciones de los reactores",
         required: [ "pais" ],
         properties: {
            ciudad: {
               bsonType: "string",
               description: "'ciudad' Debe ser una cadena de caracteres y no puede ser nulo"
            },
            pais: {
               bsonType: "string",
               description: "'pais' Debe ser una cadena de caracteres y no puede ser nulo"
            }
         }
      }
   }
} );

-- Crear Collection "reactores"

db.createCollection("reactores", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         title: "Reactores detallado",
         required: [ "nombre", "potencia_termica", "estado" ],
         properties: {
            nombre: {
               bsonType: "string",
               description: "'nombre' Debe ser una cadena de caracteres y no puede ser nulo"
            },
            potencia_termica: {
               bsonType: "number",
               minimum:0,
               description: "'potencia_termica' Debe ser una cadena de caracteres y no puede ser nulo"
            },
            primera_fecha_reaccion: {
               bsonType: "string",
               description: "'primera_fecha_reaccion' Debe ser una cadena de caracteres"
            },
            estado: {
               bsonType: "string",
               description: "'estado' Debe ser una cadena de caracteres y no puede ser nulo"
            },
            tipo_reactor_id:{
                bsonType: "objectId",
                description: "'tipo_reactor_id' Deber ser un valor de tipo ObjectId existente en la colección 'tipos_reactor'"
            },
            ubicacion_id:{
                bsonType: "objectId",
                description: "'ubicacion_id' Deber ser un valor de tipo ObjectId existente en la colección 'ubicaciones'"
            }
         }
      }
   }
} );