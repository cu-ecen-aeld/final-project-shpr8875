use paho_mqtt as mqtt;
use std::process;

fn main() {
    // MQTT connection options
    let create_opts = mqtt::CreateOptionsBuilder::new()
        .server_uri("tcp://localhost:1883") // Change to your broker URI if needed
        .client_id("rust_subscriber")
        .finalize();

    // Create a new MQTT client
    let client = match mqtt::Client::new(create_opts) {
        Ok(c) => c,
        Err(e) => {
            eprintln!("Error creating the client: {}", e);
            process::exit(1);
        }
    };

    // Connect to the MQTT broker
    if let Err(e) = client.connect(None) {
        eprintln!("Error connecting to broker: {}", e);
        process::exit(1);
    }

    // Subscribe to a topic
    if let Err(e) = client.subscribe("test/topic", 1) {
        eprintln!("Error subscribing to topic: {}", e);
        process::exit(1);
    }

    println!("Subscribed to 'test/topic'. Waiting for messages...");

    // Start consuming messages
    let receiver = client.start_consuming();

    // Process incoming messages in a loop
    for msg in receiver.iter() {
        if let Some(msg) = msg {
            println!("Received message: {}", msg);
        } else {
            println!("Disconnected or no more messages.");
            break;
        }
    }

    // Disconnect from the broker
    if let Err(e) = client.disconnect(None) {
        eprintln!("Error disconnecting: {}", e);
    }

    println!("Disconnected from broker.");
}

