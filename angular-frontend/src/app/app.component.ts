import { Component, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { GetvectorService } from './GetvectorService.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [
    GetvectorService
  ]
})
export class AppComponent {
  title = 'angular-frontend';

  // get form
  @ViewChild('f', { static: false }) inputForm: NgForm;

  vector = ''
  word = ''

  constructor(private gvs: GetvectorService) {
  }

  onSubmit() {
    // console.log(this.inputForm.value.word);
    var word = this.inputForm.value.word

    this.gvs.getVector(word).subscribe(data => {
      console.log(data);
      this.vector = data.vector
    })
  }
}
