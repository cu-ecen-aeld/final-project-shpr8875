use serde::{Serialize, Deserialize};
use serde_json;

#[derive(Serialize, Deserialize, Debug)]
struct Person {
    name: String,
    age: u32,
}

fn main() {
    // Create a new Person instance
    let person = Person {
        name: String::from("Alice"),
        age: 30,
    };

    // Serialize the Person struct into a JSON string
    let serialized = serde_json::to_string(&person).unwrap();
    println!("Serialized: {}", serialized);

    // Deserialize the JSON string back into a Person struct
    let deserialized: Person = serde_json::from_str(&serialized).unwrap();
    println!("Deserialized: {:?}", deserialized);
}

