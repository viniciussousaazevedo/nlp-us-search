import { Component } from '@angular/core';

@Component({
  selector: 'app-user-fruit',
  templateUrl: './user-fruit.component.html'
})
export class UserFruitComponent {
  userName: string = '';
  selectedFruit: string = '';
  fruits: string[] = ['Apple', 'Banana', 'Grape', 'Mango', 'Strawberry'];
  submitted = false;

  associate() {
    if (this.userName && this.selectedFruit) {
      this.submitted = true;
      console.log(`${this.userName} likes ${this.selectedFruit}`);
    }
  }
}
