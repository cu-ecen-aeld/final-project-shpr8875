use paho_mqtt as mqtt;
use std::{process, time::Duration};

fn main() {
    // MQTT connection options
    let create_opts = mqtt::CreateOptionsBuilder::new()
        .server_uri("tcp://localhost:1883") // Change to your broker URI if needed
        .client_id("rust_subscriber")
        .finalize();

    // Create a new MQTT client
    let mut client = match mqtt::Client::new(create_opts) {
        Ok(c) => c,
        Err(e) => {
            eprintln!("Error creating the client: {}", e);
            process::exit(1);
        }
    };

    // Set a message callback to process incoming messages
    client.set_message_callback(|_client, msg| {
        if let Some(message) = msg {
            println!("Received message: {:?}", message);
        }
    });

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

    // Start the MQTT client loop to receive messages
    client.start_consuming();

    // Sleep for a while to keep the subscriber active
    std::thread::sleep(Duration::from_secs(60));

    // Disconnect from the broker
    if let Err(e) = client.disconnect(None) {
        eprintln!("Error disconnecting: {}", e);
    }

    println!("Disconnected from broker.");
}

