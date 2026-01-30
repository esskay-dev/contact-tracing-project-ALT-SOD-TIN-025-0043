from contact_tracing import add_person, add_contact, get_high_risk_contacts, infection_status, contacts

# Sample data

add_person("Folami", False)
add_person("Miguel", True)
add_person("Peter", False)
add_person("Zack", False)
add_person("Salako", True)
add_person("Adeola", False)
add_person("Noah", False)
add_person("Kenny", True)
add_person("Yinka", False)
add_person("Nimi", True)

add_contact("Folami", "Miguel", 70)
add_contact("Zack", "Salako", 30)
add_contact("Salako", "Zack", 30)
add_contact("Adeola", "Salako", 10)
add_contact("Nimi", "Zack", 20)
add_contact("Noah", "Adeola", 32)

def print_report():
    high_risk = get_high_risk_contacts()

    print("\nExposure Report")
    print("------------")
    print(f"Total People: {len(infection_status)}")
    print(f"Total Contact Events: {len(contacts)}")
    print(f"Infected People: {sum(infection_status.values())}")
    print(f"High Risk Individuals: {len(high_risk)}")

    print("\nTop Exposures:")
    for exposed, infected, time in high_risk:
        print(f"-{exposed} exposed to {infected} for {time} minutes")

# Run report
print_report()