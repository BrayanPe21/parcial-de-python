import { Component, OnInit} from '@angular/core';
import {HttpClient}from '@angular/common/http'
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']

})
export class AppComponent implements OnInit {
  
  constructor(private http:HttpClient){}

  obj:any;

  ngOnInit(): void{
    this.obj = this.http.get("http://127.0.0.1:8000/api/crud/").subscribe(
    data =>this.obj = data
    )
  }

  title = 'pagina';
}
