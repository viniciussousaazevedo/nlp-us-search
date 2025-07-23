import { Component } from '@angular/core';

@Component({
  selector: 'app-example',
  templateUrl: './example.component.html'
})
export class ExampleComponent {
  fruits: string[] = ['Apple', 'Banana', 'Cherry', 'Mango', 'Strawberry'];
  selectedFruit: string = '';
  comment: string = '';
  submitted = false;

  submitChoice() {
    if (this.selectedFruit) {
      this.submitted = true;
      console.log('Selected fruit:', this.selectedFruit);
      console.log('Comment:', this.comment);
    }
  }
}
