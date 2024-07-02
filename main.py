from Databases import Erreur as err

# Example usage
db_path = 'erreurs.db'
erreur_db = err.Erreur()

# Insert records
erreur_db.insert('12345', 10.5, 22.3, 100, 150, 50.5, 50.0, 0.5, 'Sample EMT')
erreur_db.insert('67890', 11.5, 23.3, 101, 151, 51.5, 51.0, 0.6, 'Another EMT')

# Update a record
erreur_db.update_by_id(1, debitActuel=12.0, temperature=24.0)

# Delete a record
erreur_db.delete_by_id(2)

# Get all records
print(erreur_db.get_all_records())

# Find a record by id
print(erreur_db.find_by_id(1))