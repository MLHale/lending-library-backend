# Lending Library Backend API
This Backend API is written using the Django framework. It allows for the following functionality:
* The UserProfile model allows storing of user information and identifies special user roles if applicable.
* The Organization model stores address information related to a user so that shipping services can be provided.
* The Item model allows the physical equipment to be mapped to specific records in the database.
* The ItemType model describes an item and provides an image path.
* The Cart model allows the user to place items into a cart before placing an order.
* The Package model allows users to place an order for a predefined group of items so that they do not have to be added to the cart individually.
* The Order model allows tracking of the order status along with the items associated with the order.
* The History model can be used to migrate completed orders into a separate data set so that active orders can be queried quickly.


# License
The Lending Library App is a search-oriented library management app for maintaining the UNO lending library.
Copyright (C) 2019 Matt Hale and CYBR 4580/8950 Class.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
