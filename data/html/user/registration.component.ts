import { Component } from '@angular/core';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html'
})
export class RegisterComponent {
  user = {
    name: '',
    email: '',
    password: '',
    type: ''
  };

  submitted = false;

  registerUser() {
    if (this.user.name && this.user.email && this.user.password && this.user.type) {
      this.submitted = true;
      console.log('User registered:', this.user);
    }
  }
}
