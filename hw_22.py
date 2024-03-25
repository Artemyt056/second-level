from peewee import *


class Album(Model):
    AlbumId = AutoField(primary_key=True)
    Title = CharField(max_length=160, null=False)
    ArtistId = AutoField

    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'Album'


class Artist(Model):
    ArtistId = AutoField(primary_key=True)
    Name = CharField(max_length=120, null=True)

    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'Artist'


class Customer(Model):
    CustomerId = AutoField(primary_key=True)
    FirstName = CharField(max_length=40, null=False)
    LastName = CharField(max_length=20, null=False)
    Company = CharField(max_length=80, null=True)
    Address = CharField(max_length=70, null=True)
    City = CharField(max_length=40, null=True)
    State = CharField(max_length=40, null=True)
    Country = CharField(max_length=40, null=True)
    PostalCode = CharField(max_length=10, null=True)
    Phone = CharField(max_length=24, null=True)
    Fax = CharField(max_length=24, null=True)
    Email = CharField(max_length=60, null=False)
    SupportRepId = IntegerField()

    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'Customer'


class Employee(Model):
    EmployeeId = AutoField(primary_key=True)
    LastName = CharField(max_length=20, null=False)
    FirstName = CharField(max_length=20, null=False)
    Title = CharField(max_length=30, null=True)
    ReportsTo = IntegerField
    BirthDate = DateTimeField
    HireDate = DateTimeField
    Address = CharField(max_length=70, null=True)
    City = CharField(max_length=40, null=True)
    State = CharField(max_length=40, null=True)
    Country = CharField(max_length=40, null=True)
    PostalCode = CharField(max_length=10, null=True)
    Phone = CharField(max_length=24, null=True)
    Fax = CharField(max_length=24, null=True)
    Email = CharField(max_length=60, null=False)

    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'Employee'


class Images(Model):
    image_id = IntegerField
    Genre = TextField
    Image = BlobField(null=False)

    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'Images'


class Invoice(Model):
    InvoiceId = AutoField(primary_key=True)
    CustomerId = AutoField
    InvoiceDate = DateTimeField(null=False)
    BillingAddress = CharField(max_length=70, null=True)
    BillingCity = CharField(max_length=40, null=True)
    BillingState = CharField(max_length=40, null=True)
    BillingCountry = CharField(max_length=40, null=True)
    BillingPostalCode = CharField(max_length=10, null=True)
    Total = DecimalField(max_digits=10, decimal_places=2, null=False)

    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'Invoice'


class InvoiceLine(Model):
    InvoiceLineId = AutoField(primary_key=True)
    InvoiceId = AutoField
    TrackId = AutoField
    UnitPrice = DecimalField(max_digits=10, decimal_places=2, null=False)
    Quantity = AutoField

    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'InvoiceLine'


class MediaType(Model):
    MediaTypeId = AutoField(primary_key=True)
    Name = CharField(max_length=120, null=True)

    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'MediaTypeId'


class Playlist(Model):
    PlaylistId = AutoField(primary_key=True)
    Name = CharField(max_length=120, null=True)

    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'Playlist'


class PlaylistTrack(Model):
    PlaylistId = AutoField(primary_key=True)
    TrackId = AutoField

    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'PlayLisTrack'


class Genre(Model):
    GenreId = AutoField(primary_key=True)
    Name = CharField(max_length=120, null=True)

    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'Genre'


class Track(Model):
    TrackId = AutoField
    Name = CharField(max_length=200, null=False)
    AlbumId = IntegerField
    MediaTypeId = AutoField
    GenreId = IntegerField
    Composer = CharField(max_length=220, null=True)
    Milliseconds = AutoField
    Bytes = IntegerField
    UnitPrice = DecimalField(max_digits=10, decimal_places=2, null=False)

    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'Track'


genre_request_where_name_longer_than_8 = Genre.select().where(fn.LENGTH(Genre.Name) > 8)

for genre in genre_request_where_name_longer_than_8:
    print(genre.__dict__)

request_album_titles = Album.select(Album.Title)
album_titles = []
for album in request_album_titles:
    album_titles.append(album.Title)

print(album_titles)
