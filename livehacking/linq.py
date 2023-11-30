# IList<Person> personen = new List<Person>();

# personen.Add(new Person("Michael", "Ammer"));
# personen.Add(new Person("Walter", "Bauer"));
# personen.Add(new Person("Stefan", "Schneider"));

# foreach (var person in personen.Where(p=>p.Nachname == "Bauer").Select(p=>p.Nachname))
# {
#     Console.WriteLine(person);
# }
# public record Person (string Vorname, string Nachname);
